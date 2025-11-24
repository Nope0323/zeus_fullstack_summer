import React from "react";
import Greeting from "./components/Greeting";
import Profile from "./components/Profile";
import Button from "./components/Button";
import Card from "./components/Card";
import ProductCard from "./components/ProductCard";

// functional component
function App() {
  // jsx -javaScript XML
  const elements = <h1>Hello World</h1>
  // react fragment 
  // root element ганц root element байна эсвэл хоосон 
  // br/ img/ tag 
  // js  бичих бол  заавал буюу угалзан хаалтанд бичнэ.
  return (
    <div className="" id="">
      <div style={{display: "flex", flexWrap: "wrap"}}>
        <ProductCard
          title="Laptop"
          price={500000}
          description="Өндөр чадалтай орчин үеийн зөөврийн компьютер."
          imageUrl="https://images.unsplash.com/photo-1517336714731-489689fd1ca8"
          inStock={true}
        />
        <ProductCard
          title="Smartphone"
          price={1500000}
          description="Шинэ загварын ухаалаг гар утас."
          imageUrl="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=1760&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
          inStock={false}
        />
      </div>
      <Card>
        <h2>Гарчиг</h2>
        <p>Энэ бол картын дотрох текст байна.</p> 
      </Card>
      <Card>
        <h3>Өөр карт</h3>
        <ul>
          <li>Зүйл Нэг</li>
          <li>Зүйл Хоёр</li>
          <li>Зүйл Гурав</li>
        </ul>
      </Card>
      {elements}
      <Greeting />
      <Button text="Click Me" />
      <Button text="Click Me" color="red" />
      <Profile width={200} height={300} name="Togs-Erdene" age={15} profession="Monk" imgUrl="https://images.unsplash.com/photo-1658891389224-43441d0ea8ac?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8bW9ua3xlbnwwfHwwfHx8MA%3D%3D" />
      <Profile width={200} height={300} name="Bold-Erdene" age={24} profession="Software Engineer" imgUrl="https://images.unsplash.com/photo-1763013373779-19e259f95b41?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw1fHx8ZW58MHx8fHx8" />
    </div>
  )
}

export default App
