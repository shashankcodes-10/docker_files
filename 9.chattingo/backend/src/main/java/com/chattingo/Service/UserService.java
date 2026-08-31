package com.chattingo.Service;

import java.util.List;

import com.chattingo.Exception.UserException;
import com.chattingo.Model.User;
import com.chattingo.Payload.UpdateUserRequest;

public interface UserService {

    public User findUserById(Integer id) throws UserException;

    public User findUserProfile(String jwt) throws UserException;

    public User updateUser(Integer userId, UpdateUserRequest req) throws UserException;

    public List<User> searchUser(String query);
}
