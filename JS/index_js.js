const body = {
    setColor: function(color){
        document.querySelector('body').style.color = color;
    },
    setBgColor:function(color){
        document.querySelector('body').style.backgroundColor = color;
    }
}
function modeHandler(self) {
    const target = document.querySelector('body');
    const mode = ['day', 'night'];
    
    if (self.value === 'day') {
        body.setBgColor('black')
        body.setColor('white')
        setColor('powderblue');
        self.value = mode[1];
    }
    else {
        body.setBgColor('white')
        body.setColor('black')
        setColor('blue');
        self.value = mode[0];
    }
}
function setColor(color) {
    // jquery 적용 전 코드
    // const alist = document.querySelectorAll('a');
    // let i = 0;
    // while(i<alist.length) {
    //     alist[i].style.color = color;
    //     i = i+1;
    // }
    $('a').css('color', color)
}



