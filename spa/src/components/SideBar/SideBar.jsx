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
        <div className="hidden sm:block z-5 m-0 mr-2 float-left">
            <Sider
                className="overflow-auto fixed float-left bg-opacity-0"
                width={256}
                trigger={null}
                collapsible
                collapsed={collapsed}
                collapsedWidth={0}
            >
                <Menu
                    className="bg-cream w-64 z-10 min-h-screen"
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
                className="h-24 w-8 bg-dark-cream border-0 drop-shadow-sm z-100 translate-y-32 text-lg"
                style={{
                    writingMode: "vertical-rl",
                }}
                onClick={toggleCollapsed}
            >
                {collapsed ? "Expand" : "Collapse"}
            </button>
        </div>
    );
};
export default SideBar;
