import "./styles/main.css";

function App() {
  return (
    <>
      <header className="header">

        {/* Left: Logo + Title */}
        <div className="left">
          <img
            src="https://images.unsplash.com/photo-1604066867775-43f48e3957d8?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            className="logo"
            />
          <span className="title">Hanggai</span>
        </div>

        {/* Center: Search */}
        <div className="center">
          <input
            type="text"
            className="search"
            placeholder="Search product, supplier, order"
          />
        </div>

        <div className="right">
          <img
            src="https://img.icons8.com/ios-filled/50/000000/appointment-reminders.png"
            className="notification"
          />
          <img src="/user.jpg" className="avatar" />
        </div>

      </header>
    </>
  );
}

export default App;
