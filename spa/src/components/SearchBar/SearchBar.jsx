import { Input } from "antd";
import "../../index.css";

const SearchBar = () => {
    return (
        <Input
            bordered={false}
            placeholder="Recipes and more..."
        />
    );
};

export default SearchBar;
