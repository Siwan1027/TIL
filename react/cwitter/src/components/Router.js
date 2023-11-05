import React, { useState } from "react";
import { HashRouter as router, Route, Switch} from "react-router-dom";
import { Router } from "react-router-dom/cjs/react-router-dom.min";
import Auth from "../routes/Auth";
import Home from "../routes/Home";

const AppRouter = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(true);
    return(
        <Router>
            <Switch>
                {isLoggedIn ? (
                <>
                <Route exact path="/">
                    <Home />
                </Route>
                </> 
                ) : (
                <Route exact path="/">
                    <Auth />
                </Route>
                )}
            </Switch>
        </Router>
    );
};

export default AppRouter;