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
          <div className="menu-item">
            <DashboardIcon />
            <a href="/dashboard" className="sidebar-link">Dashboard</a>
          </div>

          <div className="menu-item">
            <InventoryIcon />
            <a href="/dashboard" className="sidebar-link">Inventory</a>
          </div>

          <div className="menu-item">
            <ReportsIcon />
            <a href="/dashboard" className="sidebar-link">Reports</a>
          </div>

          <div className="menu-item">
            <UserCircleIcon />
            <a href="/dashboard" className="sidebar-link">Suppliers</a>
          </div>

          <div className="menu-item">
            <OrdersIcon />
            <a href="/dashboard" className="sidebar-link">Orders</a>
          </div>

          <div className="menu-item">
            <ManageStoreIcon />
            <a href="/dashboard" className="sidebar-link">Manage Store</a>
          </div>
        </div>
        <div className="settings-items menu-items">
          <div className="settings-item sidebar-item">
            <SettingsIcon />
            <a href="/dashboard" className="sidebar-link">Settings</a>
          </div>
          <div className="settings-item sidebar-item">
            <LogoutIcon />
            <a href="/dashboard" className="sidebar-link">Log Out</a>
          </div>
        </div>
      </aside>
  );
}
