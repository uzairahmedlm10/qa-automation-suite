import {Given, When, Then} from "@badeball/cypress-cucumber-preprocessor";
import homepage from "../PageObjects/RegisterHomePage";

var home = new homepage()

Given("I open the ecommerce home page",()=>{

    cy.visit(Cypress.env('url')+"angularpractice/")
})

When("I type Name from database in the textbox",function(){

    home.twoWaydataBinding().eq(0).type(this.data[0])

})
Then("I verify if the other textbox with data binding is also filled",function(){

    home.twoWaydataBinding().eq(1).should('have.value',this.data[0])

})
When("I select the employment status as 'student' and verify if the 'entrepreneur' button is disabled",()=>{

    home.radiobutton1().check()
    home.disabledbutton().should('have.attr','disabled')
    home.disabledbutton().should('be.disabled')
})
Then("I select the employment status as 'Employed' and verify if the 'entrepreneur' button is disabled",()=>{

    home.radiobutton2().check()
    home.disabledbutton().should('be.disabled')

})
When("I type in the date from database",function(){

    home.dob().type(this.data[4])
})
Then("I put assertion to verify if the correct date has been filled in",function(){

    home.dob().should('have.value',this.data[4])
})
When("I fill in the form from database",function(){

    home.email().type(this.data[1])
    home.email().type(this.data[2])
})
Then("I click submit and put assertion to verify if the correct alert message appears",()=>{

    home.submit().click()
    home.alert().then((text)=>{

        var alertText = text.text()
        expect(alertText.includes('Success')).to.be.true
    })

})