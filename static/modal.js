var modal = document.getElementById('formModal');
var modalBtn = document.getElementById('modalBtn');
var closeBtn = document.getElementsByClassName('closeBtn')[0];

modalBtn.addEventListener('click', openModal);
closeBtn.addEventListener('click', closeModal);
window.addEventListener('click', outsideClick);


function openModal(){
    modal.style.display = 'block';  
}
function closeModal(){
    modal.style.display = 'none';  
}   
function outsideClick(e) {
    //alert(e.target.getAttribute('id'));
    if (e.target.getAttribute('id') == null ) {
      modal.style.display = 'none';
    }
  }