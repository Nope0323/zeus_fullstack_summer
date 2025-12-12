import "../styles/sidebar.css";
import { 
  DashboardIcon,
  InventoryIcon,
  UserCircleIcon,
  ManageStoreIcon,
  ReportsIcon,
  OrdersIcon,
  SettingsIcon,
  LogoutIcon
} from "../icons/icons.jsx";

export default function Sidebar() {
  return (
    <aside className="sidebar-left">
        <div className="menu-items">
        <div className="sidebar-item">
          <DashboardIcon />
          <a href="/dashboard" className="sidebar-link">Dashboard</a>
        </div>

        <div className="sidebar-item">
        <InventoryIcon/>
        <a href="/dashboard" className="sidebar-link">Inventory</a>
        </div>

        <div className="sidebar-item">
        <ReportsIcon/>
        <a href="/dashboard" className="sidebar-link">Reports</a>
        </div>

        <div className="sidebar-item">
        <UserCircleIcon/>
        <a href="/dashboard" className="sidebar-link">Suppliers</a>
        </div>

        <div className="sidebar-item">
        <OrdersIcon />
        <a href="/dashboard" className="sidebar-link">Orders</a>
        </div>
        <div className="sidebar-item">
        <ManageStoreIcon/>
        <a href="/dashboard" className="sidebar-link">Manage Store</a>
        </div>
        <div className="sidebar-item">
        <SettingsIcon/>
            <a href="/dashboard" className="sidebar-link">Settings</a>
        </div>
        <div className="sidebar-item">
        <LogoutIcon/>
        <a href="/dashboard" className="sidebar-link">Log Out</a>
        </div>
        </div>
      </aside>
  );
}
