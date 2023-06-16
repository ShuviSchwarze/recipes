import { useEffect, useState } from "react";
import useFetch from "../../features/services/useFetch";

import { Card } from "antd";
import "../../index.css";

const { Meta } = Card;

function RecipeCard(RecipeId) {
    //const url = `http://localhost:5000/api/recipes/${RecipeId}`;
    const url = `http://localhost:5000/api/recipes/1`;
    const { content, err, loading } = useFetch(url);

    return (
        <Card className="mt-2 w-72" hoverable>
            {loading ? <>Loading</> : <>{content.data.title}</>}
        </Card>
    );
}

export default RecipeCard;
