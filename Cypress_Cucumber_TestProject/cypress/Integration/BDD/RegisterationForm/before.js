before(function(){


    cy.sqlServer("Select * from AppDemo2").then(function(result){

        this.data = result
        cy.log(result)
    })
})