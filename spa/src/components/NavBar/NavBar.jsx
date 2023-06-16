import { useState } from "react";

import { Layout, Menu, Col, Row } from "antd";
import { UserOutlined, MenuOutlined, SearchOutlined } from "@ant-design/icons";

import SearchBar from "../SearchBar/SearchBar";
import Logo from "../../assets/Logo.png";
import "../../index.css";
import "./styles.css";

const { Header } = Layout;

const NavBar = () => {
    const [current, setCurrent] = useState();

    const onDefault = (e) => {
        setCurrent(e.key);
    };

    const NavBarItems = [
        {
            label: "Home",
            key: "1",
        },
        {
            label: "Seasonal",
            key: "2",
        },
        {
            label: "Meals",
            key: "3",
        },
        {
            label: "Ingredients",
            key: "4",
        },
        {
            label: "My Pantry",
            key: "5",
        },
        {
            label: "Account",
            icon: <UserOutlined />,
            key: "6",
        },
        {
            label: "Search",
            icon: <SearchOutlined />,
            key: "7",
        }
    ];

    return (
        <Header
            className="items-center bg-cream h-16 flex-row fixed w-screen z-50"
            mode="horizontal"
        >
            <Row
                className="h-16 items-center"
                gutter={{ xs: 8, sm: 16, md: 24, lg: 32 }}
            >
                <Col
                    className="items-center text-center md:text-left inline-block float-none h-16"
                    xs={{ span: 24 }}
                    sm={{ span: 24 }}
                    md={{ span: 8 }}
                    lg={{ span: 4 }}
                >
                    <div className="relative mt-2">
                        <a href="/">
                            <img className="w-auto h-16" src={Logo} />
                        </a>
                    </div>
                </Col>
                <Col
                    className="flex items-center h-16"
                    xs={{ span: 0 }}
                    sm={{ span: 0 }}
                    md={{ span: 8 }}
                    lg={{ span: 8 }}
                >
                    <span className="hidden md:flex ml-8">
                        <SearchOutlined />
                        <SearchBar />
                    </span>
                </Col>
                <Col
                    className="flex items-center h-16"
                    xs={{ span: 0 }}
                    sm={{ span: 0 }}
                    md={{ span: 8 }}
                    lg={{ span: 12 }}
                    align="right"
                >
                    <div className="flex right-1 md:absolute items-center fixed top-8 md:w-full">
                        <Menu
                            className="bg-cream block absolute right-0 md:w-full"
                            mode="horizontal"
                            overflowedIndicator={<MenuOutlined />}
                            defaultSelectedKeys={[current]}
                            items={NavBarItems}
                        >
                            <Menu.Item>
                                <span className="hidden md:flex ml-8">
                                    <SearchOutlined />
                                    <SearchBar />
                                </span>
                            </Menu.Item>
                        </Menu>
                    </div>
                </Col>
            </Row>
        </Header>
    );
};
export default NavBar;
