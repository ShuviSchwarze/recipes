import { Layout, Menu } from "antd";
import { UserOutlined, MenuOutlined } from "@ant-design/icons";

import SearchBar from "./SearchBar";
import Logo from "../assets/Logo.png";
import "../index.css";

const { Header } = Layout;

const NavBar = () => {
    return (
        <Header
            className="flex items-center bg-cream h-16 w-full fixed z-10 shadow-sm"
            mode="horizontal"
        >
            <div className="h-12 relative md:content-center w-screen md:w-64 text-center md:text-left">
                <a href="/">
                    <img className="w-auto h-16" src={Logo} />
                </a>
            </div>
            <Menu
                className="bg-cream w-12 md:w-full block"
                mode="horizontal"
                colapsable
                overflowedIndicator={<MenuOutlined />}
                defaultSelectedKeys={["1"]}
            >
                <Menu.Item key="1">Home</Menu.Item>
                <Menu.Item key="2">Seasonal</Menu.Item>
                <Menu.Item key="3">Meals</Menu.Item>
                <Menu.Item key="4">Ingredients</Menu.Item>
                <Menu.Item key="5">My Pantry</Menu.Item>
                <Menu.Item
                    key="7"
                    className="float-right"
                    icon={<UserOutlined />}
                >
                    Account
                </Menu.Item>
                <Menu.Item key="6" className="float-right w-1/3">
                    <SearchBar />
                </Menu.Item>
            </Menu>

            <div className="smallLogo"></div>
        </Header>
    );
};
export default NavBar;
