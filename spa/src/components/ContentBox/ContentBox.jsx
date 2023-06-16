import React, { useState, useEffect } from "react";
import { Breadcrumb, Layout, Menu, theme } from "antd";
import RecipeCard from "../RecipeCard/RecipeCard";

const { Content } = Layout;

function ContentBox(children) {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    return (
        <Content className="bg-white">
            <div className="m-h-360 p-6 bg-white">
                <RecipeCard />
            </div>
        </Content>
    );
}

export default ContentBox;
