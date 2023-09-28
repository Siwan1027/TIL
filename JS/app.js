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

// 객체와 함수
const car = {
    name :'자동차',
    sound:'부릉부릉',
    drive: function drive() {
        console.log(this.sound)
    }
};

car.drive();

// 객체와 함수
const motorcycle = {
    name :'오토바이',
    sound:'부와아앙',
    // 객체 내 함수를 선언할 시 이름을 정하지 않아도 가능
    ride: function() {
        console.log(this.sound)
    }
};

motorcycle.ride();

// getter & setter
const numbers = {
    a:1,
    b:2,
    // 여기서 get 으로 함수를 선언했기 때문에
    get sum() {
        console.log('sum 함수가 실행됨');
        return this.a + this.b;
    }
};
// 
console.log(numbers.sum);
numbers.b = 5;
console.log(numbers.sum);
// 이 명령어는 실행이 안됨
// console.log(numbers.sum());

const nums = {
    _a : 1,
    _b : 2,
    sum : 3,
    calculate() {
        console.log('calculate');
        this.sum = this._a + this._b;
    },
    get a() {
        return this._a;
    },
    get b() {
        return this._b;
    },
    set a(value) {
        console.log(`a가 ${value} 로 바뀝니다.`);
        this._a = value;
        this.calculate();
    },
    set b(value) {
        console.log(`b가 ${value} 로 바뀝니다.`);
        this._a = value;
        this.calculate();
    }
};

console.log(nums.sum);
nums.a = 5;
nums.b =7;
nums.a = 9;
console.log(nums.sum);
console.log(nums.sum);
console.log(nums.sum);