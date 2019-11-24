function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
})
//calculating total price in the cart

// total price = 0 adjustments
function total_zero(){
    $('#total').text(0)
    $('#order').prop('disabled', true)
    $('#cart_count').text(0)
}
// adding an element to user's cart
$('.modal').on('click','#add', function(){
    //determining what toppings were chosen by the user
    tops = ''
    $('input[type="checkbox"]:checked').each(function(){
        tops+=($(this).val()+' ')
    })
    //checking for two types of items'sizes
    if(data['sizes'].length>0){
        console.log(user)
        $.ajax({
            url:'/{{user}}/cart/', 
            type: 'POST',
            data :{'amount':$("#amount").val(),
            'size':$('input[name="size"]:checked').val(),
            'kind_id':data['kind_id'], 'cat_id':data['cat_id'],'size_id':data[$('input[name="size"]:checked').val()]['id'],
            'user': user,
            'toppings_id':tops,}
        });
        console.log(tops)
    }
    else{
        $.ajax({
            url:'/{{user}}/cart/', 
            type: 'POST',
            data :{'amount':$("#amount").val(),
            'kind_id':data['kind_id'], 'cat_id':data['cat_id'],'size_id':false,
        'user': user,
        'toppings_id':tops}
        });
        console.log('no size')
    }
    // changing cart count indicator
    if($('#cart_count').text()==''){
        $('#cart_count').text(1)
    }else{
        $('#cart_count').text(Number($('#cart_count').text())+1)
    }
    modal.html('')
    modal.hide()
       
    
})
//deleting an element from user's cart
total_price = Number($('#total').text())
$('.del').click(function(){
    price = Number($(this).parent().parent().children('.price').text())
    id = $(this).parent().parent().attr('id')
    $.ajax({
        url:'/{{user}}/cart/',
        type: 'DELETE',
        data:{'id':id,
    'user': user}
    })
    .done(function(){
        total_price -= price
        if(Math.round(total_price)==0){
            total_zero();
        }
        $('#total').text(Math.round(total_price * 100) / 100)
        $('#'+id).remove()
        $('#cart_count').text(Number($('#cart_count').text())-1)
    })  
})
$('.del').css('cursor', 'pointer')
//new stuff below ###
// Get the modal
var modal = $("#myModal");

// Get the button that opens the modal
var btn = $(".myBtn");

// Get the <span> element that closes the modal
var span = $(".cancel");
var data = {}
// When the user clicks the button, open the modal 
btn.click(function() {
    $.ajax({
        url:'api/get/', 
        type: 'GET',
        data :{'id':$(this).parent().parent().attr('id'),
    'user': name}
    })
    .done(function(data1){
        data1 = JSON.parse(data1)
        console.log(data1['sizes'])
        toppings = ''
        for(i=0; i<data1['toppings'].length; i++){
            toppings+=`<div class="form-check d-flex justify-content-start">
            <input class="form-check-input" type="checkbox" value="${data1['toppings'][i][1]}" id="${data1['toppings'][i][0]}">
            <label class="form-check-label" for="${data1['toppings'][i][0]}">
                ${data1['toppings'][i][0]}
            </label>
        </div>`
        }
        sizes = ''
        if(data1['sizes']){
            for(i=0; i<data1['sizes'].length; i++){
            sizes+=`<div class="form-check d-flex justify-content-start">
            <input class="form-check-input" type="radio" name='size' checked value="${data1['sizes'][i]}" id="${data1['sizes'][i]}">
            <label class="form-check-label" for="${data1['sizes'][i]}">
                ${data1['sizes'][i]}
            </label>
        </div>`
            }
        }
        div = ` <div class="modal-content">
        <div method='POST' class='form'>
            <h2 class='title text-center'>${data1['cat']}: ${data1['kind']}</h2>
            <div class="form-group row">
                <label for="amount" class='col-sm-2'>Amount:</label>
                <div class='col-sm-5'>
                    <input class= 'form-control'type="number" value='1' id='amount' name='amount'>
                </div>
            </div>`
        if (data1['toppings_allowed']!=0){
            div+=` <div class="form-group row">
            <label for="toppings" class='col-sm-2'>Toppings: <span id='toppings_left'>${data1['toppings_allowed']}</span> left</label>
            <div class="col-sm-5">
                `+toppings+`
            </div>
            </div>`
        }
        if(sizes){
            div+=`<div class="form-group row">
            <label for="sizes" class='col-sm-2'>Sizes:</label>
            <div class="col-sm-5">
                `+sizes+`
            </div>`
        }
        div+=`</div>
            <div class="form-group d-flex justify-content-between">
                    <input type="submit"  id='add'class='btn btn-success col-3' value='Sbumit'>
                    <span class="cancel btn btn-danger col-3">Cancel</span>
            </div>
        </div>
        </div>`
        $('.modal').html(div) 
        console.log()
        data = data1
    })
    modal.show();
    
})
modal.on('click', 'input[type="checkbox"]', function(){
    // console.log($('input[type="checkbox"]:checked').length,data['toppings_left'])
    if(data['toppings_left']>=0){
        if($(this).prop('checked')){
            data['toppings_left']-=1
            $('#toppings_left').text(data['toppings_left'])
            if(data['toppings_left']==0){
                unchecked = $('input[type="checkbox"]:not(:checked)')
                unchecked.prop('disabled', true)
            }
        }
        else{
            data['toppings_left']+=1
            $('#toppings_left').text(data['toppings_left'])
            if(data['toppings_left']>0){
                unchecked = $('input[type="checkbox"]:not(:checked)')
                unchecked.prop('disabled', false)
            }
        }
    }
    

    // toppings_left = $('#toppings_left').text()
    // $('#toppings_left').text() = 
})
// When the user clicks on <span> (x), close the modal
// span.click(function() {
//   modal.hide();
// })
$('.modal').on('click','.cancel', function(){
    $('.modal').html('') 
    modal.hide()
})

// When the user clicks anywhere outside of the modal, close it
$(window).click(function(event) {
  if (event.target == modal[0]) {
    modal.hide()
    $('.modal').html('') 
  }
})

// making an order
$('#order').click(function(){
    items = ''
    $('.item').each(function(){
        items+=($(this).attr('id')+' ')
    })
    $.ajax({
        url: '/{{user}}/order/',
        method: 'POST',
        data:{
            'user':user,
            'items': items.substring(0,(items.length-1))
        }
    }).done(function(){
        $('#cart_body').html('')
        total_zero();
    })
})
//cancel order section
$('.cancel_order').click(function(){
    id = $(this).parent().parent().parent().attr('id')
    console.log(id)
    $.ajax({
        url:`/${user}/`,
        type: 'DELETE',
        data:{'id':id,
    'user': user}
    })
    .done(function(){
        $('#'+id).remove()
    })  
})
$('.del').css('cursor', 'pointer')