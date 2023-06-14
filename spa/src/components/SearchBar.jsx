import { Input } from "antd";

import { SearchOutlined } from "@ant-design/icons";
import "../index.css";

const SearchBar = () => {
    return (
        <div>
            {/*<div className="relative w-10 h-10 inline-block hover:invisible">Ctrl K</div>*/}
            <Input
                bordered={false}
                style={{
                    textAlign: "right",
                }}
                placeholder="Recipes and more..."
            />
            <SearchOutlined />
        </div>
    );
};

export default SearchBar;
