class homepage{

    twoWaydataBinding(){

        return cy.get("[name='name']")
    }
    radiobutton1(){

        return cy.get("#inlineRadio1")
    }
    radiobutton2(){

        return cy.get("#inlineRadio2")
    }
    disabledbutton(){
        
        return cy.get("#inlineRadio3")
    }
    dob(){

        return cy.get("[name='bday']")
    }
    email(){

        return cy.get("[name='email']")
    }
    password(){

        return cy.get("#exampleInputPassword1")
    }
    submit(){

        return cy.get(".btn.btn-success")
    }
    alert(){

        return cy.get(".alert.alert-success.alert-dismissible")
    }
}
export default homepage