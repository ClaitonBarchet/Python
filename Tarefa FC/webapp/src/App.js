import './App.css';

const texto=document.querySelector("#texto");

const endpoint="lista.txt"

fetch(endpoint)
.then(res=>(console.log(res)))
.then(res=>{
  console.log(res);
})

function App() {
  return (
    <div className="App">
      
      

    </div>
  );
}

export default App;
