document.querySelectorAll('.vote_average').forEach(function(element) {
    if (element.innerHTML >= 7.5) {
        element.style.backgroundColor = '#12ff26';
    } else if (element.innerHTML < 5)  {
        element.style.backgroundColor = 'red';
    } else if (element.innerHTML > 5 && element.innerHTML < 7.5) {
        element.style.backgroundColor = '#fffb00';
    }
    
  });

/*if (voteAverage.innerHTML > 7){
    voteAverage.style.backgroundColor = 'red'
}*/


