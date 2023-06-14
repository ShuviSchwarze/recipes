import { ContainerOutlined } from "@ant-design/icons";
import { Menu, Layout } from "antd";
import { useState } from "react";
const SideBar = () => {
    const [collapsed, setCollapsed] = useState(false);
    const { Sider } = Layout;
    const toggleCollapsed = () => {
        setCollapsed(!collapsed);
    };
    return (
        <Layout className="top-16">
            <div className="hidden sm:block h-[calc(100vh-64px)] w-66 fixed z-5 top-16 overflow-auto m-0 float-left">
                <Sider
                    className="h-[calc(100vh-64px)] bg-cream overflow-auto m-0 block float-left"
                    width={256}
                    trigger={null}
                    collapsible
                    collapsed={collapsed}
                    collapsedWidth={0}
                >
                    <Menu
                        className="bg-cream w-64 z-10 h-[calc(100vh-64px)]"
                        defaultOpenKeys={["sub1"]}
                        mode="inline"
                        inlineCollapsed={collapsed}
                    >
                        <Menu.Item
                            className="text-base left-0"
                            icon={<ContainerOutlined />}
                        >
                            Ingredients
                        </Menu.Item>
                    </Menu>
                </Sider>
                <button
                    className="h-8 w-24 bg-dark-cream border-0 drop-shadow-sm -translate-x-8 z-100 translate-y-32 text-lg rotate-90"
                    onClick={toggleCollapsed}
                >
                    {collapsed ? "Expand" : "Collapse"}
                </button>
            </div>
        </Layout>
    );
};
export default SideBar;
