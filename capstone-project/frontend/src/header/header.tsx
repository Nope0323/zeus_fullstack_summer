import"../styles/header.css";
import{
UserCircleIcon,
NotificationIcon
}from"../icons/icons.jsx";
export default function Header() {
  return (
    <header className="header">
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
            <div className="sidebar--item userCircleIcon">
                <UserCircleIcon/>
            </div>
        </div>  
     </header>
  );
} 