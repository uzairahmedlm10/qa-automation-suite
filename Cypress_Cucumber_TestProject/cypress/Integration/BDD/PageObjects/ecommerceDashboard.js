class ecommerce_dashboard{

    getblinkingnotification(){

        return cy.get("div div label[class='m-2 blink_me']").then(($e1)=>{

            let notification = $e1.text()
            return notification
        })
    }
    gettoast(){

        return cy.get("div[role='alert']",{timeout: 4000})
    }
    addtocart(){

        return cy.get('div div button:nth-child(4)')
    }
    searchbox(){

        return cy.get("[formcontrolname='productName']:visible")
    }
    getproducts(){
        var productName = []
        return cy.get("div div h5 b").each(($e1,index,$list)=>{

            productName.push($e1.text())
            
        }).then(()=>{

            return productName 
        })
    }
    cartpage(){
        
        return cy.get(':nth-child(4) > .btn')
    }

    ordersbtn(){

        return cy.get("[routerlink='/dashboard/myorders']")
    }

}
export default ecommerce_dashboard