import {Given, When, Then} from "@badeball/cypress-cucumber-preprocessor";
import library_home from "../PageObjects/LibraryHome";
import library_catalogue from "../PageObjects/LibraryCatalogue";

var libhome = new library_home()
var libcatalogue = new library_catalogue()

Given("I open the library home page",()=>{

    cy.visit(Cypress.env('url')+"angularAppdemo/")
})
When("I make the api request to open the library catalogue and intercept the api response",()=>{

    cy.intercept(
        { 
            method: 'GET', 
            url: 'https://rahulshettyacademy.com/Library/GetBook.php?AuthorName=shetty' 
        },
        {
            status: 200,
            body: 
            [
                {
                    "book_name": "RestAssured with Java",
                    "isbn": "BSG",
                    "aisle": "2302"
                }
            ]

        }
    
    ).as('getBooks')
    libhome.libButton().click()
})
Then("I verify the number of books in the catalogue",()=>{
    
    cy.wait('@getBooks').then(({request,response})=>{

        libcatalogue.getrows().should('have.length', response.body.length)
    })

})
Then("I put assertion on the notification message",()=>{

    libcatalogue.getNoti().should('have.text','Oops only 1 Book available')
})

When("I intercept the api call and change request user to verify authentication",()=>{

    cy.intercept("GET","https://rahulshettyacademy.com/Library/GetBook.php?AuthorName=shetty",(req)=>{

        req.url = "https://rahulshettyacademy.com/Library/GetBook.php?AuthorName=malhotra"
        req.continue((res)=>{

            expect(res.statusCode).to.equal(404)
        })

        }).as('ChangeUser')
})
Then("I click the library catalogue button to make the api call",()=>{

    libhome.libButton().click()
    cy.wait('@ChangeUser')

})


        
        
        
        
