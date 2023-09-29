
import logo from './logo.svg';
import './App.css';
//state 사용시 자동 생성됨
import { useState } from 'react';

function App() {

  // 데이터 바인딩
  // 변수의 경우 변수가 변경되어도 직접 리렌더링 해줘야 함
  let postName = 'Hello!World';
  // state의 경우 데이터 변경 시 자동으로 리렌더링
  // state 생성 시 디스트럭쳐링 두번째 요소는 state 변경 시 사용되는 함수!
  let [titles,changeTitle] = useState(['heeeeeeeey~', 'baaaaaaaaam', 'shhhhhhhhhhh']);
  
  // 좋아요 기능
  let [likes, changeLikes] = useState(0);

  // 이 안에 html 작성되어야 함
  return (
    // JSX 에서는 class 는 class 선언이기 때문에 className 으로 명을 선정해야함
    <div className="App">
      <div className='black-nav'>
        {/* 이런식으로 css 없이 스타일 설정도 가능 */}
        <h4>
          {/* 이렇게 변수를 넣을 수 있어요! */}
          { postName }
          </h4>
      </div>
      <div className='postList'>
        <h5>{titles[0]} <span onClick={function(){changeLikes(likes + 1)}}>👍</span> {likes} </h5>
        <p>what's goin on</p>
      </div>
      <div className='postList' 
      onClick={
        () => { // array 와 object 는 참조 데이터형이기 때문에 그냥 복제한 경우 포인터 값만 가져오는 것이기 때문에 객체 자체는 동일해서 같은 객체로 인식됨
                // 즉 새로운 객체로 복제하는 deep copy 작업이 필요
                // 여기서 `...` 은 괄호를 벗기라는 뜻
                let copyTitleList = [...titles]
                // let copyTitleList = titles;
                copyTitleList[1] = 'fixed title';
              changeTitle(copyTitleList)}}>
        <h5>{titles[1]}</h5>
        <p>what's goin on</p>
      </div>
      <div className='postList'>
        <h5>{titles[2]}</h5>
        <p>what's goin on</p>
      </div>
      <div>
        <button onClick={()=>{
          let copyTitleList = [...titles]
          copyTitleList = copyTitleList.sort()
          changeTitle(
            copyTitleList)
            }
            }>sort!</button>
      </div>
    </div>
  );
}

export default App;
