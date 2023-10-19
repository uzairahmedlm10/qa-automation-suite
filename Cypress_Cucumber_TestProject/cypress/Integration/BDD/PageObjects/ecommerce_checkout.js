class ecommerce_checkout{

checkoutbutton(){

    return cy.get('.subtotal > ul > :nth-child(3) > .btn')
}
cardnumber(){
    return cy.get('input[class*="input txt text-validated"]')
}
Name_CVV(){
    return cy.get("[class='input txt']")
}
coupon(){
    return cy.get("[name='coupon']")
}
coupontext(){

    return cy.get(".mt-1.ng-star-inserted")
}
applybutton()
{

    return cy.get("[type='submit']")
}
selectCountry(){

    return cy.get("[placeholder='Select Country']")
}
searchitems() {
    
    return cy.get(".ta-results > .ng-star-inserted")
}
placeorder(){

    return cy.get(".btnn.action__submit.ng-star-inserted")
}
calendar(){
    return cy.get(".input.ddl")
}
 
downloadbtn(){
    return cy.get(".btn.btn-primary.mt-3.mb-3")
}

}
export default ecommerce_checkout