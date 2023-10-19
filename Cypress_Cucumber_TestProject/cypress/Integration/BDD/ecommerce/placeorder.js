import {Given, When, Then} from "@badeball/cypress-cucumber-preprocessor";
import ecommerce_dashboard from "../PageObjects/ecommerceDashboard";
import ecommerce_checkout from "../PageObjects/ecommerce_checkout";
import orders_page from "../PageObjects/Orders";



const neat_csv = require("neat-csv")

var orders = new orders_page()
var checkout = new ecommerce_checkout()
var dashboard = new ecommerce_dashboard()

Given("I make the api call to the ecommerce site and bypass the login page by passing the session token",()=>{

    cy.loginCall().then(()=>{

        cy.visit(Cypress.env('url')+"client", {

            onBeforeLoad: function(x){

                x.localStorage.setItem("token", Cypress.env('token'))
            }
        })
    })

})
let noti_test
When("I get the text of the blinking message",()=>{

    dashboard.getblinkingnotification().then((text)=>{

        noti_test = text
    })

    }
)
Then("I verify the text",(()=>{

    expect(noti_test).to.equal(' User can only see maximum 9 products on a page')
}))
var text
When("I add a product to the cart, I extract the toast message",()=>{

    dashboard.addtocart().eq(0).click()
    dashboard.gettoast().should('be.visible').then((toast)=>{

        text = toast.text()

    })
})
Then("I verify the text in the toast message and put assertion that notification goes away immediately",()=>{

    expect(text).to.equal(" Product Added To Cart ")
    cy.wait(4000)
    dashboard.gettoast().should('not.exist')
})
When("I type characters in the searchbox to search a product from dashboard",()=>{

    dashboard.searchbox().type("zara{enter}")
    cy.wait(3000)
    
})

Then("I put assertion on the products to verify if they have been correctly filtered based on the search result",()=>{

    dashboard.getproducts().then((products)=>{
        products.forEach(function(element) {
            cy.wrap(element).should('contain', 'zara')
        })
        
        
    })

})
let count
When("I iterate through all the products to find a specific product and add it to the cart",()=>{

    dashboard.getproducts().then((products)=>{

        for (let index = 0; index < products.length; index++) {
            const element = products[index];
            if (element.includes("iphone")) {
                count = index
                
            }
            
        }
    }).then(()=>{

    dashboard.addtocart().eq(count).click()

    })
})
Then("I go to the cart page and fill out the billing and shipping information with some assertions and apply coupon",()=>{
    dashboard.cartpage().click()
    checkout.checkoutbutton().click()
    checkout.cardnumber().eq(0).clear().type('1234 4567 1234 2345')
    checkout.Name_CVV().eq(0).type(355)
    checkout.Name_CVV().eq(1).type('XYZ')
    checkout.coupon().type("rahulshettyacademy")
    checkout.applybutton().click().then(()=>{

        checkout.coupontext().then(($e1)=>{

            let couptext = $e1.text()
            cy.wrap(couptext).should('include','Coupon Applied')
        })
    })
    
    checkout.selectCountry().type('ind')
    checkout.searchitems().each(($e1, index, $list)=>{
        if ($e1.text() === ' India') {
            cy.wrap($e1).click()
        }            
    })
    checkout.calendar().eq(0).select('12').should('have.value',12)
    checkout.calendar().eq(1).select('20').should('have.value',20)
    checkout.placeorder().click() 
    cy.wait(2000)   
})

Then("I download the order details in a csv file and verify data inside with assertions",()=>{

    checkout.downloadbtn().eq(0).click()
    cy.readFile("C:\\Users\\User\\Downloads\\order-invoice_uzairahmed914.csv").then(async (text)=>
    {

    const txtfile = await neat_csv(text)
    const Actualproduct = txtfile[0]["Product Name"]
        
        expect(Actualproduct).to.equal("iphone 13 pro")

    })


})
let totalorders
When("I go to the orders page and count the total number of orders",()=>{

    
    dashboard.ordersbtn().click()
    orders.orders_row().then((count)=>{

        totalorders = count
    })
    

})
Then("I delete an order and verify the number again",(()=>{

    
    orders.deleteFirstOrder().click()
    cy.wait(2000)
    orders.orders_row().then((count1)=>{
        expect(count1).to.equal(totalorders - 1)

    })
    
    })
    
)
