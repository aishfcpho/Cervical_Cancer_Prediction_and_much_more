class HomeController < ApplicationController
    def index
        @user_data = current_user.user_data
    end
end
