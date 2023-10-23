before(function(){

    cy.fixture('example.json').then((data)=>{

        this.data = data
    })

})