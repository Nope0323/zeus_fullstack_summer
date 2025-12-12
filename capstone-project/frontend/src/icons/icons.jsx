
export const DashboardIcon = ({ size = 28, color = "#000000ff" }) => (
    <svg
    width={size}
    height={size}
    viewBox="0 0 24 24"
    fill="none"
    stroke={color}
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
    >
      <path d="M3 9.5L12 3l9 6.5V20a1 1 0 0 1-1 1h-6v-6H10v6H4a1 1 0 0 1-1-1V9.5z" />
    </svg>
  );
  // REPORTS ICON
  export const ReportsIcon = ({ size = 28, color = "#000000ff" }) => (
      <svg 
      width={size}
      height={size}
      viewBox="0 0 24 24" 
      fill="none"
      stroke={color} 
      strokeWidth="2"
      >
      <path d="M5 3h14v18H5z"/>
      <path d="M9 17V10M12 17V7M15 17v-4"/>
    </svg>
  );
  // Inventory ICON
  export const InventoryIcon = ({ size = 28, color = "#000000ff" }) => (
    <svg 
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none" 
      stroke={color} 
      strokeWidth="2"
    >
      <path d="M3 3h2l3.6 7.59-.96 1.72A1 1 0 0 0 8.5 14H19"/>
      <circle cx="9" cy="20" r="1.5"/>
      <circle cx="17" cy="20" r="1.5"/>
    </svg>
  );
  
  
  //ManageStore ICON
  export const ManageStoreIcon = ({ size = 28, color = "#000000ff" }) => (
    <svg 
    width={size}
    height={size}
    viewBox="0 0 24 24"
    fill="none" 
    stroke={color} 
    strokeWidth="2"
    >
      <path d="M9 11l2 2 4-4"/>
      <path d="M9 17l2 2 4-4"/>
      <rect x="3" y="4" width="18" height="18" rx="2"/>
    </svg>
  );
  
  
  //Orders ICON
  export const OrdersIcon = ({ size = 28, color = "#000000ff" }) => (
    <svg 
      width={size}
      height={size}
      viewBox="0 0 24 24" 
      fill="none"
      stroke={color} 
      strokeWidth="2"
      >
      <path d="M3 7l9-4 9 4v10l-9 4-9-4z"/>
      <path d="M3 7l9 4 9-4"/>
      <path d="M12 11v10"/>
    </svg>
  );
  
  // HOME ICON
  export const HomeIcon = ({ size = 28, color = "#000000ff" }) => (
      <svg 
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke={color}
      strokeWidth="2"
      >
      <path d="M3 9.5L12 3l9 6.5V20a1 1 0 0 1-1 1h-6v-6H10v6H4a1 1 0 0 1-1-1V9.5z"/>
    </svg>
  );
  
  
  // notification ICON
 export const NotificationIcon = ({ size = 24, color = "#000" }) => (
  <svg
    width={size}
    height={size}
    viewBox="0 0 24 24"
    fill={color}
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M12.022 2c-2.188 0-4.1 1.778-4.1 3.966v2.676c-1.012.447-1.8 1.501-1.8 2.698v3.4l-.9 1.8v.9h14v-.9l-.9-1.8v-3.4c0-1.197-.788-2.251-1.8-2.698v-2.676c0-2.188-1.912-3.966-4.1-3.966zm0 20.4c1.327 0 2.4-1.07 2.4-2.4h-4.8c0 1.33 1.073 2.4 2.4 2.4z" />
  </svg>
);

  
  // SETTINGS ICON
  export const SettingsIcon = ({ size = 28, color = "#000000ff" }) => (
      <svg 
      width={size}
      height={size}
      viewBox="0 0 24 24" 
      fill="none"
      stroke={color}
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="3" />
      <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09a1.65 1.65 0 0 0-1-1.51 1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09a1.65 1.65 0 0 0 1.51-1 1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H10a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V10c0 .69.36 1.31.94 1.66.58.35.94.97.94 1.66V15z"/>
    </svg>
  );
  
  // USER AVATAR ICON (sidebar-д ашиглагддаг)
  export const UserCircleIcon = ({ size = 28, color = "#000000ff" }) => (
      <svg 
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke={color}
      strokeWidth="2"
      >
      <circle cx="12" cy="8" r="4" />
      <path d="M4 20c0-4 4-6 8-6s8 2 8 6" />
    </svg>
  );
  
  
  export const LogoutIcon = ({ size = 28, color = "#000000ff" }) => (
      <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke={color}
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      >
      <path d="M15 3H5v18h10" />
      <path d="M10 12h10" />
      <path d="M17 9l3 3-3 3" />
    </svg>
  );