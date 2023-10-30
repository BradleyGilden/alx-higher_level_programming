$('DIV#toggle_header').click(() => {
  if ($('header').hasClass('green')) {
    $('header').addClass('red').removeClass('green');
  } else {
    $('header').addClass('green').removeClass('red');
  }
});
