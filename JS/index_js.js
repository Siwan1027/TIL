function modeHandler(self) {
    const target = document.querySelector('body');
    const mode = ['day', 'night'];
    if (self.value === 'day') {
        target.style.backgroundColor = 'black';
        target.style.color = 'white';
        self.value = mode[1];
    }
    else {
        target.style.backgroundColor = 'white';
        target.style.color = 'black';
        self.value = mode[0];
    }
}
