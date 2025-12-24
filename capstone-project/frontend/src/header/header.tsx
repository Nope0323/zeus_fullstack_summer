import "../styles/header.css";
import {
  UserCircleIcon,
  NotificationIcon,
} from "../icons/icons.jsx";
import type { CSSProperties } from "react";

type HeaderProps = {
  style?: CSSProperties;
};

const Header = ({ style }: HeaderProps) => {
  return (
    <header className="header" style={style}>
      <div className="search-side">
        <input
          type="text"
          className="search"
          placeholder="Search product, supplier, order"
        />
      </div>

      <div className="user-side">
        <div className="notificationIcon">
          <NotificationIcon />
        </div>
        <div className="sidebar-item userCircleIcon">
          <UserCircleIcon />
        </div>
      </div>
    </header>
  );
};

export default Header;
