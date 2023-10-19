class library_catalogue
{

    getrows(){

        return cy.get("tbody tr")
    }
    getNoti(){

        return cy.get('p')
    }

}
export default library_catalogue