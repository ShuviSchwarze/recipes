import { bool, string } from "prop-types";

import { Card } from "antd";
import "../../index.css";

const { Meta } = Card;

RecipeCard.propTypes = {
    title: string,
    description: string,
    error: string,
    loading: bool,
};

function RecipeCard(props) {
    return (
        <Card hoverable loading={props.loading}>
            <Meta title={props.title} description={props.description} />
        </Card>
    );
}

export default RecipeCard;
