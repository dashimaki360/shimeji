var app = new Vue({
    el: '.main',
    data:{      //ここで定義した値がv-model="hoge"や{{hoge}}の初期値に反映される
        url:"127.0.0.1:5000/action",//v-model="url"の初期値
        param:"{'type': 'mist',
                 'param': {'sec':'4'}
               }",             //v-model="param"の初期値
    },
    methods: {
      handleClick: function (event) {
        config = {
            headers:{
              'X-Requested-With': 'XMLHttpRequest',
              'Content-Type':'application / x-www-form-urlencoded'
            },
            withCredentials:true,
          }
        //  param = JSON.parse(this.param)
          axios.post(this.url,this.param,config)
        alert('Ajaxを投げるよ') // [object HTMLButtonElement]
      }
    }
  })