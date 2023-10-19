class vegHomePage{

searchBox(){

    return cy.get(".search-keyword")
}
addtocart(){

    return cy.get("div[class='product']").each(($e1, index, $list)=>{

        cy.wrap($e1).contains("ADD TO CART").click()
    })
}
cartbutton(){

    return cy.get("[src*=bag]")
}
checkoutbutton(){

    return cy.contains("PROCEED TO CHECKOUT")
}
vegPrice(){
    var count = 0
    return cy.get("div[class='product']").find("p[class='product-price']").each(($e1, index, $list)=>{
        var val = Number($e1.text())
        count = count + val
    
    }).then(()=>
    {
        return count
    })
}

getcartprice(){

    return cy.get('tbody tr:nth-child(2) td:nth-child(3)').then(($e1)=>{

        var total = Number($e1.text())
        return total 
    })
}

promobox(){

    return cy.get('.promoCode')
}
applybutton(){

    return cy.get('.promoBtn' )
}
discountperc(){
    let discount
    return cy.get(".discountPerc").then(($e1)=>{

        discount = $e1.text()
        return discount
        
    })
}
totalamnt(){

    return cy.get(".totAmt").then(($e1)=>{

        let totalamount = Number($e1.text())
        return totalamount
    })
}
totalamountafterdiscount(){

    return cy.get(".discountAmt").then(($e1)=>{

        let discounted = Number($e1.text())
        return discounted
    })
}
dropdown(){

    return cy.get('select')
}
placeOrder(){

    return cy.get('button:nth-child(14)')
}
ProceedBtn(){

    return cy.get('button')
}
getAlert(){

    return cy.get('.errorAlert b').then(($e1)=>{

        let alertText = $e1.text()
        return alertText
    })
}
terms_conditionscheckbox(){

    return cy.get('.chkAgree')
}
getSuccessnoti(){

    return cy.get('.wrapperTwo').then(($e1)=>{
        let success = $e1.text()
        return success

    })
}
childtab(){

    return cy.get('div a').invoke("removeAttr", 'target')
}
homepage(){

    return cy.get('div a')
}
cartitem_total(){
    let price = 0
    return cy.get("tbody tr td:nth-child(5) p").each(($e1,index,$list)=>{

        let vegPrice = $e1.text()
        price = Number(vegPrice) + price

    }).then(()=>{

        return price
    })}
}
export default vegHomePage;

