import { ConfigProvider, Layout } from "antd";
import NavBar from "../components/NavBar/NavBar";
import SideBar from "../components/SideBar/SideBar";
import ContentBox from "../components/ContentBox/ContentBox";
import RecipeCard from "../components/RecipeCard/RecipeCard";
import "../index.css";

const Root = () => {
    return (
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
            <Layout>
                <NavBar />
                <Layout className="mt-16 overflow-hidden">
                    <SideBar />
                    <Layout className="overflow-auto max-h-[calc(100vh-64px)]">
                        <ContentBox/>
                    </Layout>
                </Layout>
            </Layout>
        </ConfigProvider>
    );
};
export default Root;
