// JS 객체 구조분해
const ironMan = {
    name : '토니 스타크',
    actor : '로다주',
    alias : '아이언 맨',
};

const captainAmerica = {
    name : '스티븐 로저스',
    actor : '크리스 에반스',
    alias : '캡틴',
};

function print(hero) {
    // JS 객체 구조분해
    // printTwo 에 보이는 방식으로 매번 객체명을 앞에 붙여서 사용해야 하는 것을 줄여줌
    const {name , actor, alias} = hero;
    const text = `${alias}(${name}) 역할은 맡은 배우는 ${actor} 이다..`
    console.log(text)
}

print(ironMan)
print(captainAmerica)

function printTwo(hero) {
    const text = `${hero.alias}(${hero.name}) 역할은 맡은 배우는 ${hero.actor} 이다..`
    console.log(text)
}

printTwo(ironMan)
printTwo(captainAmerica)

// 함수의 파라미터(인자) 단계에서 객체 비구조화 할당 가능
function printThree({alias, name, actor}) {
    const text = `${alias}(${name}) 역할은 맡은 배우는 ${actor} 이다..`
    console.log(text)
}


printThree(ironMan)
printThree(captainAmerica)