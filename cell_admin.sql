/*
 Navicat Premium Data Transfer

 Source Server         : docker_mysql8
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : 127.0.0.1:3306
 Source Schema         : cell_admin

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 15/12/2021 14:53:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for idx_user
-- ----------------------------
DROP TABLE IF EXISTS `idx_user`;
CREATE TABLE `idx_user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `nickname` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `account` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `password` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `password_salt` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `level_password` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '二级密码',
  `top_id` int NOT NULL DEFAULT '0',
  `is_delete` int NOT NULL DEFAULT '0',
  `is_freeze` int NOT NULL DEFAULT '0',
  `register_time` date DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of idx_user
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for idx_user_data
-- ----------------------------
DROP TABLE IF EXISTS `idx_user_data`;
CREATE TABLE `idx_user_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL DEFAULT '0',
  `key` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `value` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of idx_user_data
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for idx_user_fund
-- ----------------------------
DROP TABLE IF EXISTS `idx_user_fund`;
CREATE TABLE `idx_user_fund` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL DEFAULT '0',
  `币种` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `金额` decimal(11,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of idx_user_fund
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for log_admin
-- ----------------------------
DROP TABLE IF EXISTS `log_admin`;
CREATE TABLE `log_admin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `admin_id` int DEFAULT '0',
  `说明` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `备用1` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `备用2` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `备用3` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `备用4` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `备用5` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `操作时间` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of log_admin
-- ----------------------------
BEGIN;
INSERT INTO `log_admin` VALUES (29, 1, '添加文章标签/分类/属性:[\'asd\']', '', '', '', '', '', '2021-12-15 14:41:20.108271');
INSERT INTO `log_admin` VALUES (30, 1, '添加文章:asd', '', '', '', '', '', '2021-12-15 14:41:46.425527');
INSERT INTO `log_admin` VALUES (31, 1, '修改文章的浏览量+1,文章id为8', '', '', '', '', '', '2021-12-15 14:42:26.475369');
INSERT INTO `log_admin` VALUES (32, 1, '修改文章的浏览量+122,文章id为8', '', '', '', '', '', '2021-12-15 14:42:44.147277');
COMMIT;

-- ----------------------------
-- Table structure for log_user
-- ----------------------------
DROP TABLE IF EXISTS `log_user`;
CREATE TABLE `log_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT '0',
  `说明` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `备用1` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `备用2` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `备用3` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `备用4` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `备用5` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `操作时间` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of log_user
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for log_user_fund
-- ----------------------------
DROP TABLE IF EXISTS `log_user_fund`;
CREATE TABLE `log_user_fund` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL DEFAULT '0',
  `币种` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `金额` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `说明` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `备注` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `流水时间` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of log_user_fund
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for sys_ad
-- ----------------------------
DROP TABLE IF EXISTS `sys_ad`;
CREATE TABLE `sys_ad` (
  `ad_id` int NOT NULL AUTO_INCREMENT,
  `标题` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `广告位` int NOT NULL DEFAULT '0',
  `sign` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `图片` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `值` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `富文本` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`ad_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of sys_ad
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for sys_admin
-- ----------------------------
DROP TABLE IF EXISTS `sys_admin`;
CREATE TABLE `sys_admin` (
  `admin_id` int NOT NULL AUTO_INCREMENT COMMENT '管理员id',
  `role_id` int NOT NULL COMMENT '角色id',
  `account` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '账号',
  `password` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '密码',
  `password_salt` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '盐',
  `nickname` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '昵称',
  `is_delete` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of sys_admin
-- ----------------------------
BEGIN;
INSERT INTO `sys_admin` VALUES (1, 1, 'root', '42960a50f11334ea5bcba697e67bc7b0', 'BJPrExO9', 'root', 0);
INSERT INTO `sys_admin` VALUES (2, 2, 'admin', '2be3fe794b7d2e04f63a2d2b5672cf36', '706694', 'admin', 0);
COMMIT;

-- ----------------------------
-- Table structure for sys_article
-- ----------------------------
DROP TABLE IF EXISTS `sys_article`;
CREATE TABLE `sys_article` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category_id` int NOT NULL,
  `tag_ids` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `attribute_ids` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `intro` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `keyword` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `author` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `image` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `insert_time` datetime NOT NULL,
  `is_delete` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of sys_article
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for sys_article_data
-- ----------------------------
DROP TABLE IF EXISTS `sys_article_data`;
CREATE TABLE `sys_article_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `article_id` int NOT NULL DEFAULT '0',
  `key` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `value` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of sys_article_data
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for sys_article_tag
-- ----------------------------
DROP TABLE IF EXISTS `sys_article_tag`;
CREATE TABLE `sys_article_tag` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `image` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `is_delete` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of sys_article_tag
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for sys_catalog
-- ----------------------------
DROP TABLE IF EXISTS `sys_catalog`;
CREATE TABLE `sys_catalog` (
  `catalog_id` int NOT NULL AUTO_INCREMENT,
  `名称` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `图标` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `路由` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `排序` int NOT NULL DEFAULT '99',
  `上级id` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`catalog_id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of sys_catalog
-- ----------------------------
BEGIN;
INSERT INTO `sys_catalog` VALUES (1, '开发者中心', 'fa-slideshare', '', 90, 0);
INSERT INTO `sys_catalog` VALUES (2, '资源管理', 'fa-folder-open', '', 99, 0);
INSERT INTO `sys_catalog` VALUES (3, '表单', '', '/admin/resource/表单', 10, 2);
INSERT INTO `sys_catalog` VALUES (5, '目录管理', '', '/admin/sys/目录', 1, 1);
INSERT INTO `sys_catalog` VALUES (6, '表格', '', '/admin/resource/表格', 5, 2);
INSERT INTO `sys_catalog` VALUES (14, '提示框', '', '/admin/resource/提示框', 40, 2);
INSERT INTO `sys_catalog` VALUES (16, '加载按钮', '', '/admin/resource/加载按钮', 45, 2);
INSERT INTO `sys_catalog` VALUES (19, '图标', '', '/admin/resource/图标', 55, 2);
INSERT INTO `sys_catalog` VALUES (21, '徽章', '', '/admin/resource/徽章', 65, 2);
INSERT INTO `sys_catalog` VALUES (22, '栅格', '', '/admin/resource/栅格', 70, 2);
INSERT INTO `sys_catalog` VALUES (23, '模块管理', '', '/admin/sys/模块', 5, 1);
INSERT INTO `sys_catalog` VALUES (32, '管理设置', 'fa-sign-in', '', 10, 0);
INSERT INTO `sys_catalog` VALUES (33, '角色管理', '', '/admin/adm/角色', 1, 32);
INSERT INTO `sys_catalog` VALUES (34, '管理员管理', '', '/admin/adm/管理员', 2, 32);
INSERT INTO `sys_catalog` VALUES (35, '系统设置', 'fa-cogs', '', 20, 0);
INSERT INTO `sys_catalog` VALUES (36, '广告设置', '', '/admin/set/广告', 10, 35);
INSERT INTO `sys_catalog` VALUES (38, 'CSS辅助', '', '/admin/resource/css辅助', 80, 2);
INSERT INTO `sys_catalog` VALUES (39, '参数设置', '', '/admin/set/参数', 5, 35);
INSERT INTO `sys_catalog` VALUES (40, '会员管理', 'fa-user', '', 50, 0);
INSERT INTO `sys_catalog` VALUES (41, '会员列表', '', '/admin/user/会员/1', 1, 40);
INSERT INTO `sys_catalog` VALUES (42, '文章管理', 'fa-tasks', '', 60, 0);
INSERT INTO `sys_catalog` VALUES (43, '标签管理', '', '/admin/article/文章标签', 1, 42);
INSERT INTO `sys_catalog` VALUES (44, '文章管理', '', '/admin/article/文章/1', 2, 42);
INSERT INTO `sys_catalog` VALUES (45, '日志管理', 'fa-file-text-o', '', 70, 0);
INSERT INTO `sys_catalog` VALUES (46, '管理员操作日志', '', '/admin/log/管理员操作日志/1', 5, 45);
INSERT INTO `sys_catalog` VALUES (47, '会员操作日志', '', '/admin/log/会员操作日志/1', 10, 45);
INSERT INTO `sys_catalog` VALUES (48, '会员资金流水日志', '', '/admin/log/会员资金流水日志/1', 15, 45);
COMMIT;

-- ----------------------------
-- Table structure for sys_module
-- ----------------------------
DROP TABLE IF EXISTS `sys_module`;
CREATE TABLE `sys_module` (
  `module_id` int NOT NULL AUTO_INCREMENT,
  `名称` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `路由` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `上级id` int NOT NULL DEFAULT '0',
  `排序` int NOT NULL DEFAULT '99',
  PRIMARY KEY (`module_id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of sys_module
-- ----------------------------
BEGIN;
INSERT INTO `sys_module` VALUES (9, '广告模块', '', 0, 10);
INSERT INTO `sys_module` VALUES (10, '广告列表', '/admin/set/广告', 9, 1);
INSERT INTO `sys_module` VALUES (17, '修改广告表单', '/admin/set/修改广告/<int:id>', 9, 7);
INSERT INTO `sys_module` VALUES (18, '修改广告提交', '/admin/set/修改广告提交/<int:id>', 9, 8);
INSERT INTO `sys_module` VALUES (20, '参数设置模块', '', 0, 5);
INSERT INTO `sys_module` VALUES (21, '参数管理列表', '/admin/set/参数', 20, 1);
INSERT INTO `sys_module` VALUES (22, '参数值设置提交', '/admin/set/参数值提交', 20, 2);
INSERT INTO `sys_module` VALUES (23, '角色管理模块', '', 0, 2);
INSERT INTO `sys_module` VALUES (24, '角色管理列表', '/admin//adm/角色', 23, 1);
INSERT INTO `sys_module` VALUES (25, '添加角色表单', '/admin/adm/添加角色', 23, 2);
INSERT INTO `sys_module` VALUES (26, '添加角色提交', '/admin/adm/添加角色提交', 23, 3);
INSERT INTO `sys_module` VALUES (27, '修改角色表单', '/admin/adm/修改角色/<int:id>', 23, 4);
INSERT INTO `sys_module` VALUES (28, '修改角色提交', '/admin/adm/修改角色提交/<int:id>', 23, 5);
INSERT INTO `sys_module` VALUES (29, '修改角色权限表单', '/admin/adm/修改角色权限/<int:id>', 23, 6);
INSERT INTO `sys_module` VALUES (30, '修改角色权限提交', '/admin/adm/修改角色权限提交/<int:id>', 23, 7);
INSERT INTO `sys_module` VALUES (31, '删除角色提交', '/admin/adm/删除角色提交/<int:id>', 23, 8);
INSERT INTO `sys_module` VALUES (32, '管理员管理模块', '', 0, 3);
INSERT INTO `sys_module` VALUES (33, '管理员管理列表', '/admin/adm/管理员', 32, 1);
INSERT INTO `sys_module` VALUES (34, '添加管理员表单', '/admin/adm/添加管理员', 32, 2);
INSERT INTO `sys_module` VALUES (35, '添加管理员提交', '/admin/adm/添加管理员提交', 32, 3);
INSERT INTO `sys_module` VALUES (36, '修改管理员表单', '/admin/adm/修改管理员/<int:id>', 32, 4);
INSERT INTO `sys_module` VALUES (37, '修改管理员提交', '/admin/adm/修改管理员提交/<int:id>', 32, 5);
INSERT INTO `sys_module` VALUES (38, '管理员角色设置', '/admin/adm/管理员角色设置/<int:id>', 32, 6);
INSERT INTO `sys_module` VALUES (39, '删除管理员提交', '/admin/adm/删除管理员提交/<int:id>', 32, 7);
INSERT INTO `sys_module` VALUES (40, '会员管理', '', 0, 20);
INSERT INTO `sys_module` VALUES (41, '会员管理列表', '/admin/user/会员', 40, 1);
INSERT INTO `sys_module` VALUES (42, '添加会员表单', '/adminuser/添加会员', 40, 2);
INSERT INTO `sys_module` VALUES (43, '添加会员提交', '/admin/user/添加会员提交', 40, 3);
INSERT INTO `sys_module` VALUES (44, '会员编辑表单', '/admin/user/会员编辑/<int:id>', 40, 4);
INSERT INTO `sys_module` VALUES (45, '会员编辑提交', '/admin/user/会员编辑提交/<int:id>/<int:code>', 40, 5);
INSERT INTO `sys_module` VALUES (46, '会员详情', '/admin/user/会员详情', 40, 6);
INSERT INTO `sys_module` VALUES (47, '会员充值表单', '/admin/user/会员充值/<int:id>', 40, 7);
INSERT INTO `sys_module` VALUES (48, '会员充值提交', '/admin/user/会员充值提交/<int:id>', 40, 8);
INSERT INTO `sys_module` VALUES (49, '冻结会员操作', '/user/冻结会员提交/<int:id>', 40, 9);
INSERT INTO `sys_module` VALUES (50, '删除会员提交', '/admin/user/删除会员提交/<int:id>', 40, 10);
INSERT INTO `sys_module` VALUES (51, '文章管理模块', '', 0, 30);
INSERT INTO `sys_module` VALUES (52, '文章标签管理列表', '/admin/article/文章标签', 51, 1);
INSERT INTO `sys_module` VALUES (53, '添加文章标签表单', '/admin/article/添加文章标签/<string:category>', 51, 2);
INSERT INTO `sys_module` VALUES (54, '添加文章标签提交', '/admin/article/添加文章标签提交/<string:category>', 51, 3);
INSERT INTO `sys_module` VALUES (55, '修改文章标签表单', '/admin//article/修改文章标签/<int:id>', 51, 4);
INSERT INTO `sys_module` VALUES (56, '修改文章标签提交', '/admin/article/修改文章标签提交/<int:id>', 51, 5);
INSERT INTO `sys_module` VALUES (57, '删除文章标签提交', '/admin/article/删除文章标签提交/<int:id>', 51, 6);
INSERT INTO `sys_module` VALUES (58, '文章管理列表', '/admin/article/文章', 51, 7);
INSERT INTO `sys_module` VALUES (59, '添加文章表单', '/admin/article/添加文章', 51, 8);
INSERT INTO `sys_module` VALUES (60, '添加文章提交', '/admin/article/添加文章提交', 51, 9);
INSERT INTO `sys_module` VALUES (61, '修改文章表单', '/admin/article/修改文章/<int:id>', 51, 10);
INSERT INTO `sys_module` VALUES (62, '修改文章提交', '/admin/article/修改文章提交/<int:id>', 51, 11);
INSERT INTO `sys_module` VALUES (63, '删除文章提交', '/admin/article/删除文章提交/<int:id>', 51, 12);
COMMIT;

-- ----------------------------
-- Table structure for sys_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_role`;
CREATE TABLE `sys_role` (
  `role_id` int NOT NULL AUTO_INCREMENT,
  `角色名` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `备注` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `权限` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of sys_role
-- ----------------------------
BEGIN;
INSERT INTO `sys_role` VALUES (1, '开发者', '拥有全部权限,无法删除', '');
INSERT INTO `sys_role` VALUES (2, '超级管理员', '与开发者权限平级, 但可进行更改', ',10,11,13,15,16,17,19,');
COMMIT;

-- ----------------------------
-- Table structure for sys_setting
-- ----------------------------
DROP TABLE IF EXISTS `sys_setting`;
CREATE TABLE `sys_setting` (
  `id` int NOT NULL AUTO_INCREMENT,
  `上级id` int NOT NULL DEFAULT '0',
  `标题` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `类型` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `值` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `备注` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `排序` int NOT NULL DEFAULT '99',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of sys_setting
-- ----------------------------
BEGIN;
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
