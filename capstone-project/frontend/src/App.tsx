import "./styles/main.css";


function App() {
  return (
    <>
      <header className="header">
        <div className="center">
          <input
            type="text"
            className="search"
            placeholder="Search product, supplier, order"
          />
        </div>

        <div className="right">
          <svg fill="black" width="22" height="22" viewBox="0 0 24 24">
            <path d="M12 24c1.1 0 2-.9 2-2h-4c0 1.1.9 2 2 2zm6-6v-5c0-3.1-1.6-5.6-4.5-6.3V6c0-.8-.7-1.5-1.5-1.5S10.5 5.2 10.5 6v.7C7.6 7.4 6 9.9 6 13v5l-2 2v1h16v-1l-2-2z" />
          </svg>

          <svg 
            width="28" 
            height="28" 
            viewBox="0 0 24 24" 
            fill="none" 
            stroke="#000000ff" 
            stroke-width="2">
            <circle cx="12" cy="8" r="4" />
            <path d="M4 20c0-4 4-6 8-6s8 2 8 6" />
            </svg>
        </div>
      </header>

      <aside className="sidebar--left">
        <img
          src="https://images.unsplash.com/photo-1604066867775-43f48e3957d8?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
          className="logo"
        />

        <div className="menu-items">
          <div className="dashboard-item">
            <svg 
              width="28" 
              height="28" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="#000000ff" 
              stroke-width="2">
            <path d="M3 9.5L12 3l9 6.5V20a1 1 0 0 1-1 1h-6v-6H10v6H4a1 1 0 0 1-1-1V9.5z"/>
            </svg>
             <a href="/dashboard" className="dashboard-link">Dashboard</a>
          </div>

          <div className="Inventory-item">
            <svg 
            width="28" 
            height="28" 
            viewBox="0 0 24 24" 
            fill="none" 
            stroke="#221111ff" 
            strokeWidth="2">
            <path d="M3 3h2l3.6 7.59-.96 1.72A1 1 0 0 0 8.5 14H19"/>
            <circle cx="9" cy="20" r="1.5"/>
            <circle cx  ="17" cy="20" r="1.5"/>
            </svg>
            <a href="/dashboard" className="inventory-link">Inventory</a>
          </div>

          <div className="Reports-item">
            <svg 
            width="28" 
            height="28" 
            viewBox="0 0 24 24" 
            fill="none" 
            stroke="#4b5563" 
            stroke-width="2">
            <path d="M5 3h14v18H5z"/>
            <path d="M9 17V10M12 17V7M15 17v-4"/>
            </svg>
            <a href="/dashboard" className="reports-link">Reports</a>
          </div>

          <div className="Suppliers-item">
            <svg 
            width="28" 
            height="28" 
            viewBox="0 0 24 24" 
            fill="none" 
            stroke="#4b5563" 
            stroke-width="2">
            <circle cx="12" cy="8" r="4" />
            <path d="M4 20c0-4 4-6 8-6s8 2 8 6" />
            </svg>
            <a href="/dashboard" className="suppliers-link">Suppliers</a>
          </div>
          
          <div className="Orders-item">
            <svg 
            width="28" 
            height="28" 
            viewBox="0 0 24 24" 
            fill="none" 
            stroke="#4b5563" 
            stroke-width="2">
            <path d="M3 7l9-4 9 4v10l-9 4-9-4z"/>
            <path d="M3 7l9 4 9-4"/>
            <path d="M12 11v10"/>
            </svg>
              <a href="/dashboard" className="orders-link">Orders</a>
          </div>
          <div className="ManageStore-item">
            <svg 
              width="28" 
              height="28" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="#4b5563" 
              stroke-width="2">
              <path d="M9 11l2 2 4-4"/>
              <path d="M9 17l2 2 4-4"/>
              <rect x="3" y="4" width="18" height="18" rx="2"/>
              </svg>
              <a href="/dashboard" className="manageStore-link">Manage Store</a>
          </div>
          <div className="Settings-item">
            <svg 
            width="28" 
            height="28" 
            viewBox="0 0 24 24" 
            fill="none"
            stroke="#000000ff"
            stroke-width="2" 
            stroke-linecap="round" 
            stroke-linejoin="round">
              <circle cx="12" cy="12" r="3" />
              <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09a1.65 1.65 0 0 0-1-1.51 1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09a1.65 1.65 0 0 0 1.51-1 1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H10a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V10c0 .69.36 1.31.94 1.66.58.35.94.97.94 1.66V15z"/>
              </svg>
              <a href="/dashboard" className="settings-link">Settings</a>
          </div>
          <div className="LogOut-item">
           <svg 
           width="28" 
           height="28" 
           viewBox="0 0 24 24" 
           fill="none"
           stroke="#000000ff" 
           stroke-width="2" 
           stroke-linecap="round" 
           stroke-linejoin="round">
            <path d="M15 3H5v18h10" />
            <path d="M10 12h10" />
            <path d="M17 9l3 3-3 3" />
            </svg>
            <a>Log Out</a> 
          </div>
        </div>
      </aside>
      <main>
        <div className="salesOverview">
          <h2>
            hi
          </h2>
              
        </div>
        <div className="sales">

              
        </div>

      </main>
    </>
  );
}

export default App;
