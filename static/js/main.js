var updateBtns = document.getElementsByClassName('update-cart')

for (i=0; i< updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        // var user = '{{request.username}}';
        var productId = this.dataset.product
        var action=this.dataset.action
        
        console.log('prductId:',productId,'Action:',action)
        console.log('USER:',user)

        updateUserOrder(productId,action)    
    })
}

function updateUserOrder(productId,action){
    console.log('User is authenticated,sending data')

    var url='/update_item/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId,'action':action})
    })
    .then((response) => {
        return response.json();
    })
    .then((date) => {
        location.reload()
    })
}