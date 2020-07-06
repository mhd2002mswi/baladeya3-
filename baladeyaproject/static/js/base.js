  var image =document.images
  var loadimage = document.createElement('img')
  loadimage.onload = function () {
    image.src=this.src
  }
  setTimeout(function () {

      loadimage.src='{% static "img/test.jpg" %}'
  },1000)
