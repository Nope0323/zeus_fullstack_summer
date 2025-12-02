import "./styles/main.css";
import { 
  DashboardIcon,
  NotificationIcon,
  InventoryIcon,
  UserCircleIcon,
  ManageStoreIcon,
  ReportsIcon,
  OrdersIcon,
  SettingsIcon,
  LogoutIcon
} from "./icons/icons.jsx";


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
          <div className="notificationIcon">
            <NotificationIcon size={28} color="#000" />
          </div> 
          <div className="userCircleIcon">
            <UserCircleIcon size={28} color="#000" />
          </div>
        </div>
      </header>

      <aside className="sidebar--left">
      


        <div className="menu-items">
          <div className="dashboard-item">
            <DashboardIcon size={28} color="#1d4ed8" />
            <a href="/dashboard" className="dashboard-link">Dashboard</a>
          </div>

          <div className="Inventory-item">
            <InventoryIcon size={28} color="#1d4ed8" />
            
            <a href="/dashboard" className="inventory-link">Inventory</a>
          </div>

          <div className="Reports-item">
            <ReportsIcon size={28} color="#1d4ed8" />
            <a href="/dashboard" className="reports-link">Reports</a>
          </div>

          <div className="Suppliers-item">
            <UserCircleIcon size={28} color="#1d4ed8" />
            <a href="/dashboard" className="suppliers-link">Suppliers</a>
          </div>
          
          <div className="Orders-item">
            <OrdersIcon size={28} color="#1d4ed8" />
            <a href="/dashboard" className="orders-link">Orders</a>
          </div>
          <div className="ManageStore-item"> 
            <ManageStoreIcon size={28} color="#1d4ed8" />
            <a href="/dashboard" className="manageStore-link">Manage Store</a>
          </div>
          <div className="Settings-item">
          <SettingsIcon size={28} color="#000" />
              <a href="/dashboard" className="settings-link">Settings</a>
          </div>
          <div className="LogOut-item">
            <LogoutIcon size={28} color="#000" />
             <span>Log Out</span>
          </div>
        </div>
      </aside>
      <main>
        
  <div className="card">
      <h2>Sales Overview</h2>
      {/* Sales content */}
  </div>

  <div className="card">
      <h2>Purchase Overview</h2>
      {/* Purchase content */}
  </div>

  {/* Дахин олон card нэмж болно */}
  <div className="card">
      <h2>New Overview</h2>
  </div>
      </main>
    </>
  );
}

export default App;
