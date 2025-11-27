# Git推送故障排查指南

## 常见错误及解决方案

### 错误1：连接超时

```
Failed to connect to github.com port 443 after 21045 ms: Couldn't connect to server
```

**原因：** 网络连接问题，HTTPS端口(443)无法访问

**解决方案：**

#### 方法1：配置代理（如果你使用代理上网）

```bash
# 如果使用HTTP代理
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890

# 如果使用SOCKS5代理
git config --global http.proxy socks5://127.0.0.1:7890
git config --global https.proxy socks5://127.0.0.1:7890

# 取消代理配置
git config --global --unset http.proxy
git config --global --unset https.proxy
```

**端口说明：**
- `7890` - Clash/V2Ray常用端口
- `10809` - V2RayN默认端口
- `1080` - 传统SOCKS代理端口

#### 方法2：修改超时时间

```bash
# 增加超时时间到10分钟
git config --global http.postBuffer 524288000
git config --global http.lowSpeedLimit 0
git config --global http.lowSpeedTime 999999
```

#### 方法3：使用SSH协议代替HTTPS

```bash
# 查看当前远程仓库配置
git remote -v

# 将HTTPS改为SSH
git remote set-url origin git@github.com:ttcai559-lgtm/tool_project.git

# 推送
git push origin main
```

**注意：** 使用SSH需要先配置SSH密钥

#### 方法4：取消SSL验证（临时方案，不推荐）

```bash
# 仅用于临时解决问题
git config --global http.sslVerify false

# 问题解决后记得恢复
git config --global http.sslVerify true
```

---

### 错误2：认证失败

```
remote: Support for password authentication was removed on August 13, 2021.
```

**原因：** GitHub不再支持密码认证

**解决方案：**

#### 使用Personal Access Token (PAT)

1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 设置权限（至少需要 `repo`）
4. 生成并复制token

**推送时使用token：**
```bash
git push https://YOUR_TOKEN@github.com/ttcai559-lgtm/tool_project.git main
```

**或者配置凭据：**
```bash
git config --global credential.helper store
# 下次推送时输入token作为密码，之后会自动保存
```

---

### 错误3：分支冲突

```
error: failed to push some refs to 'https://github.com/...'
hint: Updates were rejected because the remote contains work that you do
```

**原因：** 远程仓库有新的提交，本地仓库落后了

**解决方案：**

```bash
# 先拉取远程更新
git pull origin main --rebase

# 如果有冲突，解决后
git add .
git rebase --continue

# 推送
git push origin main
```

---

## 快速诊断流程

### 1. 测试网络连接
```bash
# Ping测试
ping github.com

# HTTPS连接测试
curl -I https://github.com

# 如果curl失败，可能是代理问题
```

### 2. 检查Git配置
```bash
# 查看所有配置
git config --global --list

# 查看远程仓库
git remote -v

# 查看代理配置
git config --global http.proxy
git config --global https.proxy
```

### 3. 测试推送
```bash
# 增加详细输出
GIT_CURL_VERBOSE=1 GIT_TRACE=1 git push origin main
```

---

## 推荐配置

### 国内用户推荐配置

```bash
# 1. 增加缓冲区大小
git config --global http.postBuffer 524288000

# 2. 设置合理的超时时间
git config --global http.lowSpeedLimit 1000
git config --global http.lowSpeedTime 60

# 3. 如果使用代理（根据实际情况）
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890

# 4. 启用凭据缓存
git config --global credential.helper store
```

### 无代理用户配置

```bash
# 1. 增加缓冲区
git config --global http.postBuffer 524288000

# 2. 取消可能存在的代理配置
git config --global --unset http.proxy
git config --global --unset https.proxy

# 3. 启用凭据缓存
git config --global credential.helper store
```

---

## 当前项目推送命令

### 使用HTTPS（需要token）
```bash
git push origin main
```

### 使用SSH（需要密钥）
```bash
# 修改远程仓库URL
git remote set-url origin git@github.com:ttcai559-lgtm/tool_project.git

# 推送
git push origin main
```

---

## 常用Git命令

```bash
# 查看状态
git status

# 查看远程仓库
git remote -v

# 查看提交历史
git log --oneline -10

# 查看配置
git config --global --list

# 强制推送（谨慎使用）
git push origin main --force

# 查看详细的推送过程
GIT_CURL_VERBOSE=1 git push origin main
```

---

## 替代方案

如果GitHub始终无法连接，可以考虑：

1. **使用Gitee镜像**
   ```bash
   git remote add gitee https://gitee.com/your-username/tool_project.git
   git push gitee main
   ```

2. **使用GitHub Desktop**
   - 图形化界面，自动处理认证

3. **使用SSH协议**
   - 更稳定，不受HTTPS限制

---

**更新日期**: 2025-11-27
