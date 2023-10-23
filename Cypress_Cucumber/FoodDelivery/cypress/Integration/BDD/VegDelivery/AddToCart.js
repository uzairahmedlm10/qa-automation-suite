import {Given, When, Then} from "@badeball/cypress-cucumber-preprocessor";
import vegHomePage from "../PageObjects/GreenCartHomePage"

var vegHome = new vegHomePage()

//I go to the ecommerce website
Given("I go to the ecommerce website", ()=>{

    cy.visit(Cypress.env("url")+"seleniumPractise/#/")

})
When("I filter vegetables from the search box",()=>{

    vegHome.searchBox().type('ca')
})
When("Add to cart",()=>{
    
    vegHome.addtocart()

})
Then("I go to the cart page",()=>{

    vegHome.cartbutton().click()
    vegHome.checkoutbutton().click()
})

Then("I verify the total price in the cart", ()=>{

    
    vegHome.vegPrice().then((count) => {
        vegHome.getcartprice().then((total) => {
          expect(count).to.equal(total);
        });
      });
    
})

Then("Apply promo code,wait and verify the discounted price", function(){
    let new_discount
    let TAD
    vegHome.promobox().type(this.data.promo)
    vegHome.applybutton().click()
    cy.wait(6000)
    vegHome.discountperc().then((discount)=>{

        new_discount = Number(discount.replace("%", ""))
        new_discount = new_discount/100
        
    })
    vegHome.totalamnt().then((total)=>{

        TAD = total * new_discount
        TAD = total - TAD
        
    })
    vegHome.totalamountafterdiscount().then((discounted)=>{

        expect(discounted).to.equal(TAD)
    })

    })

Then("select country and place order without agreeing to terms", (()=>{

    vegHome.placeOrder().click()
    vegHome.dropdown().select("Algeria").should('have.value',"Algeria")
    vegHome.ProceedBtn().click()
    vegHome.getAlert().should('contain', 'Terms & Conditions')


    })
    
)
Then("agree to terms and condition, place order and verify the 'success' message", (()=>{

    vegHome.placeOrder().click()
    vegHome.dropdown().select("Algeria").should('have.value',"Algeria")
    vegHome.terms_conditionscheckbox().check().should('be.checked')
    vegHome.ProceedBtn().click()
    vegHome.getSuccessnoti().should('contain', 
    'Thank you, your order has been placed successfully')
    


})
)

Then("I go to the terms and conditions tab and then i go to the home page",(()=>{
    vegHome.placeOrder().click()
    vegHome.childtab().click()
    vegHome.homepage().click()
    

}))
Then("I verify the url with an assertion",(()=>{
    
    cy.url().should('eq','https://rahulshettyacademy.com/seleniumPractise/#/')

}))
Then("verify if the items in the cart table makes the equal sum of the total amount mentioned",()=>{
    vegHome.cartitem_total().then((price)=>{
        vegHome.totalamnt().then((totalamount)=>{

        expect(price).to.equal(totalamount)

        })
        
    })

})
    


        