import { ConfigProvider, Layout } from "antd";
import NavBar from "../components/NavBar";
import SideBar from "../components/SideBar";
import "../index.css";

const Root = () => {
    return (
        <Layout>
            <ConfigProvider
                theme={{
                    token: {
                        colorPrimary: "#c90f45",
                        colorInfo: "#c90f45",
                        colorBgBase: "#FFFFFF",
                        colorTextBase: "#000000",
                        colorBgContainer: "#FFF6DE",
                        borderRadius: 9,
                        wireframe: false,
                    },
                }}
            >
                <NavBar />
                <Layout className="w-screen h-screen">
                    <SideBar />
                </Layout>
            </ConfigProvider>
        </Layout>
    );
};
export default Root;
