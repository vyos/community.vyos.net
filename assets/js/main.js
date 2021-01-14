$(document).ready(function(){

  const openCloseToggleIcons = $('div.header__mobile-menu__buttons img');
  
  $(openCloseToggleIcons).click(function(){

    $(openCloseToggleIcons).toggleClass('active');
    if($(this).hasClass('open')) $('nav#mobile-menu').animate({'left': '0%'}, 300);
    if($(this).hasClass('close')) $('nav#mobile-menu').animate({'left': '100%'}, 300);

  });

});