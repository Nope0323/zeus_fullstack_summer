import "../styles/sidebar.css";
import {
  DashboardIcon,
  InventoryIcon,
  UserCircleIcon,
  ManageStoreIcon,
  ReportsIcon,
  OrdersIcon,
  SettingsIcon,
  LogoutIcon,
} from "../icons/icons.jsx";
import type { CSSProperties } from "react";

type SidebarProps = {
  style?: CSSProperties;
};

const Sidebar = ({ style }: SidebarProps) => {
  return (
    <aside className="sidebar-left" style={style}>
      <div className="menu-items">
        <div className="menu-item">
          <DashboardIcon />
          <a href="/dashboard" className="sidebar-link">Dashboard</a>
        </div>
        <div className="menu-item">
          <InventoryIcon />
          <a href="/inventory" className="sidebar-link">Inventory</a>
        </div>
        <div className="menu-item">
          <ReportsIcon />
          <a href="/reports" className="sidebar-link">Reports</a>
        </div>
        <div className="menu-item">
          <UserCircleIcon />
          <a href="/suppliers" className="sidebar-link">Suppliers</a>
        </div>
        <div className="menu-item">
          <OrdersIcon />
          <a href="/orders" className="sidebar-link">Orders</a>
        </div>
        <div className="menu-item">
          <ManageStoreIcon />
          <a href="/store" className="sidebar-link">Manage Store</a>
        </div>
      </div>

      <div></div>

      <div className="menu-items settings-items">
        <div className="sidebar-item">
          <SettingsIcon />
          <a href="/settings" className="sidebar-link">Settings</a>
        </div>
        <div className="sidebar-item">
          <LogoutIcon />
          <a href="/logout" className="sidebar-link">Log Out</a>
        </div>
      </div>
    </aside>

  );
};

export default Sidebar;
