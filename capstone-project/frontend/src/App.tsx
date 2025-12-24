import "./styles/main.css";
import { Helmet } from "react-helmet";
// import { NotificationIcon, UserCircleIcon } from "./icons/icons.jsx";
import Header from "./header/header";
import Sidebar from "./sidebar/sidebar";
function App() {
  return (
    <>
      <Helmet>
        <link
          href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600&display=swap"
          rel="stylesheet"
        />
      </Helmet>

      <div className="layout-container">
        <Sidebar style={{ gridArea: "sidebar" }} />
        <Header style={{ gridArea: "header" }} />
        <main  style={{ gridArea: "main" }} >
          <div className="main-content">
            
            <div className="sales">
              <h2>Sales Overview</h2>
            </div>

            <div className="summary">
              <h2>Inventory Summary</h2>
            </div>

            <div className="sales">
              <h2>Purchase Overview</h2>
            </div>
            <div className="summary">
              <h2>Product Summary</h2>
            </div>

            <div className="graph-sale">
              <h2>Sale Purchase</h2>
            </div>

            <div className="graph-summary">
              <h2>Order Summary</h2>
            </div>

            <div className="graph-sale">
              <h2>Top Selling Stock</h2>
            </div>

            <div className="graph-summary">
              <h2>Low Quantity Stock</h2>
            </div>
          </div>
        </main>
      </div>

    </>
  );
}

export default App;
