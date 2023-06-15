let show=true;
const menuContent=document.querySelector('.content');
const menuToggle=menuContent.querySelector('.menu-toggle');


menuToggle.addEventListener('click',() => {
    document.body.style.overflow= show ? 'hidden' : 'initial'
    menuContent.classList.toggle('on',show);
    show=!show;
})
function fecharCaixa() {
    var caixa = document.getElementById('caixa-compra');
    caixa.style.display = 'none';
  }
  $(document).ready(function() {
    $('#cpf').inputmask('999.999.999-99');
  });
  