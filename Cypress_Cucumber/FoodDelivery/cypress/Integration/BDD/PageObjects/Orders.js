class orders_page{

    orders_row(){
        let count
        return cy.get('tbody tr').each(($e1, index, $list)=>{
            count = index + 1

        }).then(()=>{

            return count
        })
    }
    deleteFirstOrder(){

        return cy.get(".btn.btn-danger").eq(0)

    }

}
export default orders_page