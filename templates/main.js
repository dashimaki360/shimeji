var app = new Vue({
    el: '.main',
    methods: {
      handleClick: function (event) {
        alert('Ajaxを投げるよ') // [object HTMLButtonElement]
      }
    }
  })